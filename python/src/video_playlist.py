"""A video playlist class."""

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):
        self._name = name
        self._videos = list()
    
    @property
    def name(self):
        return self._name

    def add_video(self, video, playlist_name):
        if video not in self._videos:
            self._videos.append(video)
            message = f'Added video to {playlist_name}: {video.title}'
        else:
            message = f'Cannot add video to {playlist_name}: Video already added'
        
        print(message)

    def show_playlist(self):
        if len(self._videos) > 0:
            for video in self._videos:
                print(str(video))
        else:
            print('No videos here yet')

    def remove_video(self, video, playlist_name):
        try:
            self._videos.remove(video)
            print(f'Removed video from {playlist_name}: {video.title}')
        except ValueError:
            print(f'Cannot remove video from {playlist_name}: Video is not in playlist')

    def clear_playlist(self, playlist_name):
        self._videos.clear()
        print(f'Successfully removed all videos from {playlist_name}')
