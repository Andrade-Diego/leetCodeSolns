var reverseWords = function(s) {
    let words = s.trim().split(' ').filter(c => c !== '').map(w => w.trim())
    return words.reverse().join(' ');
};
str = "   a good   example    "
console.log(`(TEST)\n\tTest string: "${str}"\n\tReversed Words: "${reverseWords(str)}"`);
