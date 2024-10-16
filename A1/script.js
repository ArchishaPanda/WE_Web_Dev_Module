document.querySelectorAll('h1, h2, h3').forEach((heading) => {
    heading.addEventListener('click', () => {
        const content = heading.nextElementSibling;
        if (content) {
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        }
    });
});
