import os
import webbrowser

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Fresh Tomatoes!</title>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css">

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #video .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #youtube-video {
            width: 100%;
            height: 100%;
        }
        .video-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .video-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .img-responsive {
            margin: 0 auto;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .episode-number {
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 20px;
        }
    </style>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- video Video Modal -->
    <div class="modal" id="video">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="youtube-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <header class="container">
      <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Videos</a>
            <ul class="nav nav-pills">
              {nav_list}
            </ul>
          </div>
        </div>
      </nav>
    </header>
    <main class="container tab-content">
      {video_tiles}
    </main>
'''

main_page_scripts = '''
    <!-- Scripts -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#youtube-video-container").empty();
        });
        // Start playing the video whenever the video modal is opened
        $(document).on('click', '.video-tile', function (event) {
            var videoYouTubeId = $(this).attr('data-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + videoYouTubeId + '?autoplay=1&html5=1';
            $("#youtube-video-container").empty().append($("<iframe></iframe>", {
              'id': 'youtube-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Handle content setup when the page loads
        $(document).ready(function () {
          activateFirstSelection();
          delayFadeFirstPane();
        });
        // Make active items to be initially selected by default
        function activateFirstSelection() {
          activateFirstSelectorItem('li');
          activateFirstSelectorItem('.tab-pane');
        }
        // Add active class to first item of given selector
        function activateFirstSelectorItem(selector) {
          var firstSelectorItem = $(selector).first();
          firstSelectorItem.addClass('active');
        }
        // Make slight delay so first content shows fade effect
        function delayFadeFirstPane() {
          var firstPane = $('.tab-pane').first();
          var waitTime = 300;

          setTimeout(function() {
            if (firstPane.hasClass('active'))
              firstPane.addClass('in');
          }, waitTime);
        }
    </script>
  </body>
</html>
'''

# A single video entry html template
tile_content = '''
<div class="col-md-6 col-lg-4 video-tile text-center" data-youtube-id="{{youtube_id}}" data-toggle="modal" data-target="#video">
    <img class="img-responsive" src="{{thumbnail_url}}" alt="{{video_title}} thumbnail">
    {tile_label}
</div>
'''

video_tile_content = tile_content.format(tile_label='<h2>{video_title}</h2>')

episode_tile_content = tile_content.format(tile_label='''
    <h2 class="episode-number">Episode {episode_number}</h2>
    <p class="subtitle">{video_title}</p>
    ''')

nav_item_content = '''
<li><a data-toggle="pill" href="#{playlist_id}">{playlist_name}</a></li>
'''


def create_id_format(name):
    return name.replace(' ', '').lower()

def create_playlist_nav_content(playlists):
    content=''
    for playlist in playlists:
        content += nav_item_content.format(playlist_id=create_id_format(playlist.name), playlist_name=playlist.name)

    return content


def create_playlist_tiles_content(playlists):
    # The HTML content for this section of the page
    content = ''
    for playlist in playlists:
        content += '<div id="{playlist_id}" class="tab-pane fade">'.format(playlist_id=create_id_format(playlist.name))
        for video in playlist.videos:
            # Append the tile for the video with its content filled in
            try:
                content += episode_tile_content.format(
                    video_title=video.title,
                    episode_number=video.episode_number,
                    thumbnail_url=video.thumbnail_url,
                    youtube_id=video.youtube_id
                )
            except:
                content += video_tile_content.format(
                    video_title=video.title,
                    thumbnail_url=video.thumbnail_url,
                    youtube_id=video.youtube_id
                )

        content += '</div>'

    return content


def open_playlists_page(playlists):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the video tiles placeholder generated content
    rendered_content = main_page_content.format(
        nav_list=create_playlist_nav_content(playlists),
        video_tiles=create_playlist_tiles_content(playlists))

    # Output the file
    output_file.write(main_page_head + rendered_content + main_page_scripts)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
