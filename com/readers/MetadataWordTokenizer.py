class MetadataWordTokenizer:
    def tokenize(self, metadata):
        return [self._process(t.split(",")) for t in metadata.split("\n")]

    def _process(self, split):
        return tuple((split[0][1:], split[1][:-1]))
