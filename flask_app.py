# from flask import Flask, render_template, request, flash, Response
# from pytube import YouTube
# from forms import VideosLinkForm

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# @app.route('/')
# def hello_world():
#     form = VideosLinkForm()
#     return render_template('pages/home.html', form=form)

# @app.route('/extractaudio', methods=['POST'])
# def extractaudio():
#     form = VideosLinkForm(request.form)
#     error = False
#     if form.validate():
#         url = form.video_link.data
#         try:
#             video = YouTube(url)
#             stream = video.streams.filter(only_audio=True).first()
#             if stream:
#                 audio_stream = stream.stream_to_buffer()
#                 # return render_template('pages/home.html', form=form, audio_stream=audio_stream)
#                 return Response(audio_stream, content_type='audio/mpeg')
#             else:
#                 flash('No audio stream found for this video')
#                 return render_template('pages/home.html')
#         except:
#             error = True

#         finally:
#             if error == True:
#                 flash('Failed to fetch video information')
#                 return render_template('pages/home.html')
#     else:
#         flash('Could not validate Video URL')
#         return render_template('pages/home.html')
#     return render_template('pages/home.html', form=form, audio_stream=audio_stream)


# from flask import Flask, render_template, request, flash
# from pytube import YouTube
# from forms import VideosLinkForm

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# # Define your custom user agent
# CUSTOM_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# @app.route('/')
# def hello_world():
#     form = VideosLinkForm()
#     return render_template('pages/home.html', form=form, audio_stream=None)

# @app.route('/extractaudio', methods=['POST'])
# def extractaudio():
#     form = VideosLinkForm(request.form)
#     error = False
#     audio_stream = None

#     if form.validate():
#         url = form.video_link.data
#         try:
#             # Set the custom user agent in the headers
#             headers = {'User-Agent': CUSTOM_USER_AGENT}
#             video = YouTube(url, headers=headers)
#             stream = video.streams.filter(only_audio=True).first()
#             if stream:
#                 audio_stream = stream.stream_to_buffer()
#             else:
#                 flash('No audio stream found for this video')
#                 error = True
#         except Exception as e:
#             flash(f'Failed to fetch video information: {str(e)}')
#             error = True

#     else:
#         flash('Could not validate Video URL')
#         error = True

#     return render_template('pages/home.html', form=form, audio_stream=audio_stream) if not error else render_template('pages/home.html', form=form, audio_stream=None)



# from flask import Flask, render_template, request, flash
# import requests
# from pytube import YouTube
# from forms import VideosLinkForm

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# # Define your custom user agent
# CUSTOM_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# @app.route('/')
# def hello_world():
#     form = VideosLinkForm()
#     return render_template('pages/home.html', form=form, audio_stream=None)

# @app.route('/extractaudio', methods=['POST'])
# def extractaudio():
#     form = VideosLinkForm(request.form)
#     error = False
#     audio_stream = None

#     if form.validate():
#         url = form.video_link.data
#         try:
#             # Set the custom user agent in the request headers
#             headers = {'User-Agent': CUSTOM_USER_AGENT}

#             # Create a session with custom headers
#             session = requests.Session()
#             session.headers.update(headers)

#             # Fetch the video webpage content with the custom user agent
#             response = session.get(url)
#             if response.status_code == 200:
#                 # Create a YouTube object from the webpage content
#                 video = YouTube(url, defer_prefetch_init=False)
#                 stream = video.streams.filter(only_audio=True).first()
#                 if stream:
#                     audio_stream = stream.stream_to_buffer()
#                 else:
#                     flash('No audio stream found for this video')
#                     error = True
#             else:
#                 flash(f'Failed to fetch video information: Status code {response.status_code}')
#                 error = True
#         except Exception as e:
#             flash(f'Failed to fetch video information: {str(e)}')
#             error = True

#     else:
#         flash('Could not validate Video URL')
#         error = True

#     return render_template('pages/home.html', form=form, audio_stream=audio_stream) if not error else render_template('pages/home.html', form=form, audio_stream=None)



# from flask import Flask, render_template, request, flash
# from pytube import YouTube
# from forms import VideosLinkForm
# import pytube.exceptions as pytube_exceptions

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# @app.route('/')
# def hello_world():
#     form = VideosLinkForm()
#     return render_template('pages/home.html', form=form, audio_stream=None)

# @app.route('/extractaudio', methods=['POST'])
# def extractaudio():
#     form = VideosLinkForm(request.form)
#     error = False
#     audio_stream = None

#     if form.validate():
#         url = form.video_link.data
#         try:
#             video = YouTube(url)
#             stream = video.streams.filter(only_audio=True).first()
#             if stream:
#                 audio_stream = stream.stream_to_buffer()
#             else:
#                 flash('No audio stream found for this video')
#                 error = True
#         except pytube_exceptions.RegexMatchError as e:
#             flash(f'Failed to fetch video information: {str(e)}')
#             error = True
#     else:
#         flash('Could not validate Video URL')
#         error = True

#     return render_template('pages/home.html', form=form, audio_stream=audio_stream) if not error else render_template('pages/home.html', form=form, audio_stream=None)


# from flask import Flask, render_template, request, flash
# import subprocess
# from forms import VideosLinkForm

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# @app.route('/')
# def hello_world():
#     form = VideosLinkForm()
#     return render_template('pages/home.html', form=form)

# @app.route('/extractaudio', methods=['POST'])
# def extractaudio():
#     form = VideosLinkForm(request.form)
#     error = False

#     if form.validate():
#         url = form.video_link.data
#         try:
#             # Use youtube-dl to download audio
#             subprocess.run(['youtube-dl', '--extract-audio', '--audio-format', 'mp3', '-o', 'audio.mp3', url], check=True)
#         except subprocess.CalledProcessError as e:
#             flash(f'Failed to fetch video information: {str(e)}')
#             error = True
#     else:
#         flash('Could not validate Video URL')
#         error = True

#     return render_template('pages/home.html') if not error else render_template('pages/home.html')


from flask import Flask, render_template, request, flash
from pytube import YouTube
from forms import VideosLinkForm
# import fbdown
import instaloader
from moviepy.editor import VideoFileClip

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key


@app.route('/')
def hello_world():
    form = VideosLinkForm()
    return render_template('pages/home.html', form=form, audio_stream=None)

@app.route('/extractaudio', methods=['POST'])
def extractaudio():
    form = VideosLinkForm(request.form)
    error = False
    audio_stream = None

    if form.validate():
        url = form.video_link.data
        try:
            if 'youtube.com' in url:
                # Handle YouTube videos using pytube
                video = YouTube(url)
                stream = video.streams.filter(only_audio=True).first()
                if stream:
                    audio_stream = stream.stream_to_buffer()
                else:
                    flash('No audio stream found for this YouTube video')
                    error = True
            elif 'facebook.com' in url:
                # Handle Facebook videos using fbdown
                # video_url = fbdown.get(url)
                # audio_stream = fbdown.audio(video_url)
                pass
            elif 'instagram.com' in url:
                # Handle Instagram videos using instaloader with login credentials
                L = instaloader.Instaloader()

                # Provide your Instagram login credentials
                L.context.log_in("stanleychiemelapaul", "bmurc650")

                profile = instaloader.Profile.from_username(L.context, "instagram_username")
                posts = profile.get_posts()
                for post in posts:
                    if url in post.url:
                        video_url = post.url
                        # Download the video using instaloader
                        L.download_post(post, target="downloaded_videos")

                        # Load the downloaded video and extract audio using moviepy
                        video_clip = VideoFileClip("downloaded_videos/" + post.date.strftime("%Y-%m-%d_%H-%M-%S") + "_" + post.owner_username + ".mp4")
                        audio_clip = video_clip.audio
                        audio_stream = audio_clip.write_audiofile("extracted_audio.mp3")

                        break

            else:
                flash('Unsupported video source')
                error = True
        except Exception as e:
            flash('Failed to fetch video information')
            error = True

    else:
        flash('Could not validate Video URL')
        error = True

    return render_template('pages/home.html', form=form, audio_stream=audio_stream) if not error else render_template('pages/home.html', form=form, audio_stream=None)



