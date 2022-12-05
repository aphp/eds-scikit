const dfs = document.querySelectorAll('.dataframe');

// dfs.forEach(df => {
//     elem = df;
//     parent = df.parentElement

//     while (elem.offsetWidth == parent.offsetWidth) {
//         elem = parent
//         parent = parent.parentElement
//     }
//     parent.style.overflowX = 'auto';
// });


dfs.forEach(df => {
    elem = df;
    elem.style.overflowX = 'auto';
    elem.style.display = "block";
});
