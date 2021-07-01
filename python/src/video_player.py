"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
from random import choice

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing_video = None
        self._paused = False
        self._playlists = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda video: video.title, reverse=False)
        
        print("Here's a list of all available videos:")
        for video in videos:
            # title, video_id, tags = video.title, video.video_id, video.tags
            # tags = ' '.join(tags)
            print(str(video))
        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        new_video = self._video_library.get_video(video_id)
        if new_video is not None:
            if self._playing_video is not None:
                self.stop_video()
            if new_video.flagged:
                self._playing_video = None
                message = f'Cannot play video: Video is currently flagged (reason: {new_video.flag_reason})'
            else:
                self._playing_video = new_video
                message = f"Playing video: {self._playing_video.title}"
        else:
            message = "Cannot play video: Video does not exist"

        print(message)
        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        try:
            print(f"Stopping video: {self._playing_video.title}")
            self._playing_video = None
            self._paused = False
        except AttributeError:
            print(f'Cannot stop video: No video is currently playing')
        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        videos = list(filter(lambda video: not video.flagged, videos))
        if len(videos) > 0:
            video = choice(videos)
            video_id = video.video_id
            self.play_video(video_id)
        else:
            print('No videos available')
        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self._playing_video is None:
            message = f"Cannot pause video: No video is currently playing"
        elif self._paused:
            message = f"Video already paused: {self._playing_video.title}"
        else:
            self._paused = True
            message = f"Pausing video: {self._playing_video.title}"

        print(message)
        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._playing_video is None:
            message = f"Cannot continue video: No video is currently playing"
        elif self._paused:
            self._paused = False
            message = f"Continuing video: {self._playing_video.title}"
        else:
            message = f"Cannot continue video: Video is not paused"

        print(message)
        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self._playing_video is None:
            message = "No video is currently playing"
        else:
            message = f"Currently playing: {str(self._playing_video)}"

            if self._paused:
                message = f"{message} - PAUSED" 

        print(message)
        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        message = 'Cannot create playlist: A playlist with the same name already exists'
        for playlist in self._playlists:
            if playlist.name.lower() == playlist_name.lower():
                break
        else:
            new_playlist = Playlist(playlist_name)
            self._playlists.append(new_playlist)
            self._playlists.sort(key=lambda playlist: playlist.name.lower(), reverse=False)
            message = f'Successfully created new playlist: {playlist_name}'

        print(message)

        # print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        for playlist in self._playlists:
            if playlist.name.lower() == playlist_name.lower():
                selected_playlist = playlist
                break
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        
        selected_video = self._video_library.get_video(video_id)
        if selected_video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        
        if selected_video.flagged:
            print(f'Cannot add video to {playlist_name}: Video is currently flagged (reason: {selected_video.flag_reason})')
            return

        selected_playlist.add_video(selected_video, playlist_name)

        # print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlists) > 0:
            print('Showing all playlists:')
            for playlist in self._playlists:
                print(playlist.name)
        else:
            print('No playlists exist yet')

        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for playlist in self._playlists:
            if playlist.name.lower() == playlist_name.lower():
                print(f'Showing playlist: {playlist_name}')
                playlist.show_playlist()
                break
        else:
            print(f'Cannot show playlist {playlist_name}: Playlist does not exist')
        # print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        for playlist in self._playlists:
            if playlist_name.lower() == playlist.name.lower():
                selected_playlist = playlist
                break
        else:
            print(f'Cannot remove video from {playlist_name}: Playlist does not exist')
            return

        selected_video = self._video_library.get_video(video_id)
        if selected_video is None:
            print(f'Cannot remove video from {playlist_name}: Video does not exist')
            return

        selected_playlist.remove_video(selected_video, playlist_name)      

        # print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for playlist in self._playlists:
            if playlist.name.lower() == playlist_name.lower():
                playlist.clear_playlist(playlist_name)
                break
        else:
            print(f'Cannot clear playlist {playlist_name}: Playlist does not exist')
        # print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for idx, playlist in enumerate(self._playlists):
            if playlist.name.lower() == playlist_name.lower():
                del self._playlists[idx]
                print(f'Deleted playlist: {playlist_name}')
                break
        else:
            print(f'Cannot delete playlist {playlist_name}: Playlist does not exist')
        # print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        results = list(filter(lambda video: video.title.lower().find(search_term.lower()) > -1 and not video.flagged, self._video_library.get_all_videos()))

        if len(results) > 0:
            results.sort(key=lambda video: video.title.lower(), reverse=False)
            print(f'Here are the results for {search_term}:')
            for i, result in enumerate(results):
                print(f'{i+1}) {str(result)}')

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                inp = int(input())
                if 0 <= inp <= len(results):
                    video_id = results[inp-1].video_id
                    self.play_video(video_id)
            except ValueError:
                pass
        else:
            print(f'No search results for {search_term}')

        # print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        selected_videos = list()
        for video in self._video_library.get_all_videos():
            tags = list(video.tags)
            tags = [tag.lower() for tag in tags]
            if video_tag in tags:
                selected_videos.append(video)
        
        if len(selected_videos) > 0:
            selected_videos = list(filter(lambda video: not video.flagged, selected_videos))

        if len(selected_videos) > 0:
            print(f'Here are the results for {video_tag}:')
            for i, video in enumerate(selected_videos):
                print(f'{i+1}) {str(video)}')
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                inp = int(input())
                if 0 <= inp <= len(selected_videos):
                    video_id = selected_videos[inp-1].video_id
                    self.play_video(video_id)
            except ValueError:
                pass
        else:
            print(f'No search results for {video_tag}')
        # print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if video is not None:
            if self._playing_video == video:
                self.stop_video()
            if flag_reason == "":
                video.set_flagged(True)
            else:
                video.set_flagged(True, flag_reason)
        else:
            print('Cannot flag video: Video does not exist')
        # print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if video is not None:
            video.set_flagged(False)
        else:
            print('Cannot remove flag from video: Video does not exist')
        # print("allow_video needs implementation")
