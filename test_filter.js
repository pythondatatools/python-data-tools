
const navItems = [
    { "id": "04", "title": "Ch 4: NumPy Basics", "path": "/chapter/04" },
    { "id": "05", "title": "Ch 5: Pandas Intro", "path": "/chapter/05" },
    { "id": "06", "title": "Ch 6: Data Loading", "path": "/chapter/06" },
    { "id": "07", "title": "Ch 7: Data Cleaning", "path": "/chapter/07" }
];

const existingChapters = ['04', '05', '06'];

const entries = navItems
    .filter(item => !existingChapters.includes(item.id))
    .map(item => ({
        id: item.id
    }));

console.log(JSON.stringify(entries, null, 2));
