var mobytrie = new Trie();

// Populate the mobypron trie [with pronunciations]
for (var mobyword in mobypron) {
    if (mobypron.hasOwnProperty(mobyword)) {
        var fields = mobypron[mobyword].split(/\/+/);
        mobytrie.insert(fields, mobyword);
    }
}

// Populate a second trie with the words themselves
var wordTrie = new Trie();

var words = Object.keys(mobypron);
var numWords = words.length;

for (var i = 0; i < numWords; i++) {
    var word = words[i];
    wordTrie.insert(word.split(''), word);
}

/* 
 * Returns a set of words from the mobypron trie that (hopefully)
 * rhyme with the word specified by PRON_FIELDS.
 */
var fromTrie = function(pronFields) {
    if (pronFields.length > 4) {
        pronFields.splice(0, pronFields.length - 3);
    } else if (pronFields.length > 2) {
        pronFields.splice(0, pronFields.length - 2);
    }
    
    var results = mobytrie.autoComplete(pronFields);
    if (results.length == 0) {
        return ["grandfather clock"]; // hey, we've got to return something!
    }
    
    // Return a random word from results
    return [results[Math.floor(Math.random() * results.length)]];
}

/*
 * Like fromTrie, except an "s" will automatically be appended to the resulting rhyme.
 */
var pluralFromTrie = function(pronFields) {
    var rhyme = fromTrie(pronFields);
    rhyme[0] = rhyme[0].concat("s");
    return rhyme;
}

var lookup = function(word) {
    if (word.slice(-1) === "*") {
        switch (word) {
            case "n****":
                return ["gold digga"];
            case "f***":
                return ["luck"];
            case "s***":
                return ["hit"];
        }
    } else if (mobypron.hasOwnProperty(word)) {
        return fromTrie(mobypron[word].split(/\/+/));
    } else if (mobypron.hasOwnProperty(word.toLowerCase())) {
        return fromTrie(mobypron[word.toLowerCase()].split(/\/+/));
    } else {
        var singular = word.substring(0, word.length - 1);
        if (word.slice(-1) === "s" && mobypron.hasOwnProperty(singular)) {
            return pluralFromTrie(mobypron[singular].split(/\/+/));
        }
        
        var approximation = wordTrie.getApproximation(word.toLowerCase().split(''));
        if (approximation == null && word.slice(-1) === "s") { // plurality case
            approximation = wordTrie.getApproximation(singular.split(''));
            if (approximation == null) {
                return ["grandmother clock"];
            } else {
                return pluralFromTrie(mobypron[approximation].split(/\/+/));
            }
        }
        
        return fromTrie(mobypron[approximation].split(/\/+/));
    }
};
