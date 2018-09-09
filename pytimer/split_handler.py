from json   import dump, load


class SplitHandler:
    """
    Handles reading, updating, and writing from/to split files.
    """

    CURRENT_FILE_VERSION = 1.0

    VERSION_KEY = "file_version"
    TITLE_KEY = "title"
    SEGMENTS_KEY = "segments"

    def __init__(self, split_filename):
        title, segments = self._read_splitfile(split_filename)

        self.title = title
        self.segments = segments
        self._segment_index = 0

    @property
    def sum_of_best(self):
        return sum([segment.best_time for segment in self.segments])

    @property
    def difference_from_best(self):
        return sum([segment.difference for segment in self.segments])

    def _read_splitfile(self, filename):
        """
        Open and return the information from the given file.
        """
        with open(filename, 'r') as splitfile:
            split_json = load(splitfile)
        return self._parse_json(split_json)

    def _parse_json(self, split_json):
        """
        Read the relevant information from the JSON and return it.
        """
        if split_json[self.VERSION_KEY] != self.CURRENT_FILE_VERSION:
            raise RuntimeError("File version is outdated.")
        title = split_json[self.TITLE_KEY]
        segments = [self.Segment(seg_data) 
                        for seg_data in split_json[self.SEGMENTS_KEY]]
        
        return title, segments

    def save_splits(self, filename, replace):
        """
        Open and write the current split information to the given file.
        """
        with open(filename, 'w') as splitfile:
            dump(self._build_json_object(replace), splitfile, indent = 4)

    def _build_json_object(self, replace):
        """
        Create the JSON-parsable dictionary to be written out to a file.
        """
        return {self.VERSION_KEY : self.CURRENT_FILE_VERSION,
                self.TITLE_KEY : self.title,
                self.SEGMENTS_KEY : [segment.build_json_object(replace) 
                                        for segment in self.segments]}

    def set_split(self, time):
        """
        Set the next segment to the current time, and return the derived 
        information from the update.
        """
        if self._segment_index < len(self.segments):
            self.segments[self._segment_index].current_time = time

            diff = self.segments[self._segment_index].difference
            curr_index = self._segment_index

            self._segment_index += 1

            return diff, curr_index

    def skip_segment(self):
        """
        Increase the segment index, keeping it within the upper bound.
        """
        self._segment_index += 1
        n = len(self.segments)
        if self._segment_index >= n:
            self._segment_index = n

    def back_segment(self):
        """
        Decrease the segment index, keeping it within the lower bound.
        """
        self._segment_index -= 1
        if self._segment_index < 0:
            self._segment_index = 0

    class Segment:
        """
        The container for the specific information for each segment within 
        the splitfile.
        """
        
        LABEL_KEY = "segment_label"
        BEST_TIME_KEY = "best_run_time"
        
        def __init__(self, segment_dict):
            self.label = segment_dict[self.LABEL_KEY]
            self.best_time = segment_dict[self.BEST_TIME_KEY]
            self.current_time = 0.0     # in ms

        def build_json_object(self, replace):
            """
            Create the JSON-parsable dictionary to be written out to a file.
            """
            return {self.LABEL_KEY : self.label,
                    self.BEST_TIME_KEY : 
                        round(self.current_time, 4) if replace else self.best_time}

        @property
        def difference(self):
            diff = 0.0
            if self.current_time != 0.0:
                diff = self.current_time - self.best_time
            return diff
