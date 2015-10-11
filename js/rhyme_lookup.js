var mobytrie = new Trie();

// Populate the mobypron trie
for (var mobyword in mobypron) {
    if (mobypron.hasOwnProperty(mobyword)) {
        var fields = mobypron[mobyword].split(/\/+/);
        mobytrie.insert(fields, mobyword);
    }
}

var lookup = function(word) {
    var pronFields = mobypron[word].split(/\/+/);
    return mobytrie.autoComplete(pronFields);
};
