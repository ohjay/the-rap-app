var mobytrie = new Trie();

// Populate the mobypron trie
for (var mobyword in mobypron) {
    if (mobypron.hasOwnProperty(mobyword)) {
        var fields = mobypron[mobyword].split(/\/+/);
        mobytrie.insert(fields, mobyword);
    }
}

var lookup = function(word) {
    if (mobypron.hasOwnProperty(word)) {
        var pronFields = mobypron[word].split(/\/+/);
        if (pronFields.length > 4) {
            pronFields.splice(0, pronFields.length - 3);
        } else if (pronFields.length > 2) {
            pronFields.splice(0, pronFields.length - 2);
        }
        
        var results = mobytrie.autoComplete(pronFields);
        if (results.length == 0) { return []; }
        
        /* // Get the shortest word from results
        var shortestWord = results[0];
        var longestWord = null;
        for (var i = 1; i < results.length; i++) {
            var r = results[i];
            if (r.length < shortestWord.length || Math.random() > 0.42) {
                shortestWord = r;
            }
        } */
        
        // Return a random word from results
        return [results[Math.floor(Math.random() * results.length)]];
    } else {
        return [];
    }
};
