/**
 * A trie. Based on an implementation written by Saurabh Odhyan (http://odhyan.com).
 * That implementation can be found here: http://odhyan.com/blog/2010/11/trie-implementation-in-javascript/.
 * Optimized for IPA field insertion and reverse string lookup.
 * 
 * Original author: Saurabh Odhyan
 * Chronologically subsequent author: Owen Jow
 * Date: Oct 11, 2015 [shoutout to Cal Hacks!]
 */

function Trie() {
    this.word = null; // the word we've got at this point in the trie
    this.children = {};
}

Trie.prototype = {
    
    /*
     * Inserts an IPA entry into the trie (backwards).
     * Recursively traverses the trie, creating new nodes wherever they don't already exist.
     *
     * @method insert
     * @param {Array} ipaEntries IPA fields to insert [should be split on /, i.e. w/ str.split()]
     * @param {String} word The word that the overall IPA phrase is actually associated with
     * @return {Void}
     */
    insert: function(ipaEntries, word) {
        if (ipaEntries.length == 0) {
            // "It's over! It's all over!"
            this.word = word;
            return;
        }
        
        var field = ipaEntries[ipaEntries.length - 1]; // should be an IPA field str
        if (this.children[field] === undefined) {
            this.children[field] = new Trie();
        }
        
        ipaEntries.pop();
        this.children[field].insert(ipaEntries, word);
    },
    
    /*
     * Gets all of the words in the trie.
     */
    getAllWords: function() {
        var words = [], 
            c;
            
        if (this.word != null) {
            words.push(word);
        }
        
        for (c in this.children) {
            words = words.concat(this.children[c].getAllWords());
        }
        
        return words;
    },
    
    /*
     * Autocompletes the given suffix.
     * 
     * @param {Array} fields An array of IPA fields to serve as a suffix (in order!)
     * @return {Array} Array of possible suggestions
     */
    autoComplete: function(fields) {
        if (fields.length == 0) {
            return this.getAllWords();
        }
        
        child = this.children[fields[fields.length - 1]];
        if (child === undefined) {
            return [];
        } else if (fields.length === 1) {
            return child.getAllWords();
        } else {
            fields.pop();
            return child.autoComplete(fields);
        }
    }
};