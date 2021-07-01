"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._flagged = False
        self.__flag_reason = None

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flagged(self):
        return self._flagged

    @property
    def flag_reason(self):
        return self.__flag_reason

    # @flagged.setter
    def set_flagged(self, flag, flag_reason='Not supplied'):
        if self._flagged and flag:
            print('Cannot flag video: Video is already flagged')
        elif self._flagged:
            self._flagged = flag
            self.__flag_reason = None
            print(f'Successfully removed flag from video: {self.title}')
        elif flag:
            self._flagged = flag
            self.__flag_reason = flag_reason
            print(f'Successfully flagged video: {self.title} (reason: {flag_reason})')
        else:
            print('Cannot remove flag from video: Video is not flagged')

    def __str__(self):
        title, video_id, tags = self.title, self.video_id, self.tags
        tags = ' '.join(tags)
        video_str = f'{title} ({video_id}) [{tags}]'

        if self._flagged:
            video_str = f'{video_str} - FLAGGED (reason: {self.__flag_reason})'

        return video_str
