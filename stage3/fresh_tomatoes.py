import os
import webbrowser

# Page top, mostly for title, to avoid string replace conflict with CSS braces
main_page_title = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{title}</title>
'''

# Styles and scripting for the page
main_page_head = '''
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css">

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        a,
        a:hover,
        a:active,
        a:focus {
            outline: 0 none;
        }
        /* Need to override Bootstrap */
        .nav-pills > li.active > a,
        .nav-pills > li.active > a:focus,
        .nav-pills > li.active > a:hover {
            background-color: #ce4844;
        }
        .pill {
            color: #ce4844;
            margin-top: 5px;
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
            height: 2em;
            line-height: 1em;
            margin: 0;
            padding: 0;
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
      <nav class="navbar navbar-inverse navbar-fixed-top navbar-header" role="navigation">
        <a class="navbar-brand" href="#">{title}</a>
        <ul class="nav nav-pills">
          {nav_list}
        </ul>
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
        function scrollPageToTop() {
            $("html, body").animate({ scrollTop: 0 }, "slow");
        }
        $(".pill").on('click', function (event) {
            scrollPageToTop();
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
          scrollPageToTop();
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

# Setup for Video object tile
video_tile_content = tile_content.format(tile_label='<h2>{video_title}</h2>')

# Setup for Episode object tile
episode_tile_content = tile_content.format(tile_label='''
    <h2 class="episode-number">{episode_label} {episode_number}</h2>
    <p class="subtitle">{video_title}</p>
    ''')

nav_item_content = '''
<li><a class="pill" data-toggle="pill" href="#{playlist_id}">{playlist_name}</a></li>
'''


def create_id_format(name):
    """Create HTML ID from given string.

    Args:
        name: The name of an item.

    Returns:
        String: An ID-friendly version of the name.

    """
    return name.replace(' ', '').lower()


def create_playlist_nav_content(playlists):
    """Create the HTML for a navigation button for each playlist.

    Args:
        playlists: A list of playlists.

    Returns:
        String: HTML code for navigation buttons.

    """
    content = ''
    for playlist in playlists:
        content += nav_item_content.format(
            playlist_id=create_id_format(playlist.title),
            playlist_name=playlist.title)

    return content


def create_playlist_tiles_content(playlists):
    """Creates HTML for tiles for each playlist.

    Args:
        playlists: A list of playlists.

    Returns:
        String: HTML code for all playlist video tiles.

    """
    content = ''
    for playlist in playlists:
        content += '<div id="{playlist_id}" class="tab-pane fade">'.format(
            playlist_id=create_id_format(playlist.title))
        for video in playlist.videos:
            # Append the tile for the video with its content filled in
            try:
                content += episode_tile_content.format(
                    video_title=video.title,
                    episode_label=playlist.type,
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


def open_playlists_page(page_title, playlists):
    """Opens a webpage generated from the list of playlists.

    Args:
        page_title: The title of the page.
        playlists: A list of playlists.

    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    rendered_title = main_page_title.format(title=page_title)

    # Replace the video tiles placeholder generated content
    rendered_content = main_page_content.format(
        title=page_title,
        nav_list=create_playlist_nav_content(playlists),
        video_tiles=create_playlist_tiles_content(playlists))

    # Output the file
    output_file.write(
        rendered_title + main_page_head + rendered_content + main_page_scripts)
    output_file.close()

    # Open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
