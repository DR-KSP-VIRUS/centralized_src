const comments = document.querySelectorAll(".comment-sections");
const commentForms = document.querySelectorAll(".comment-forms");
const loginComment = document.getElementById("login-comment");
const commentInfo = document.getElementById("comment-info");
const closeInfo = document.getElementById("close-comment-info");


for (const key in comments) {
    if (Object.prototype.hasOwnProperty.call(comments, key)) {
        const element = comments[key];
        element.addEventListener('click', () => {
            commentForms[key].classList.toggle('hidden');
        });
    }
}

loginComment.addEventListener("click", () => {
    commentInfo.classList.replace("hidden", "flex");
});

closeInfo.addEventListener("click", () => {
    commentInfo.classList.replace("flex", "hidden");
});
