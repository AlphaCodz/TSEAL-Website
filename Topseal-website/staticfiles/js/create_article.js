const tagsSelectionEl = document.querySelector("#tags_selection");
const selectedTags = document.querySelector(".tags_select");

const tagItems = document.querySelector(".tags_select");

let tags = [];

setTags();

tagsSelectionEl.addEventListener("change", (e) => {
  if (e.target.value !== "" && !tags.includes(e.target.value)) {
    tags.push(e.target.value);
  }

  setTags();
});

selectedTags.addEventListener("mouseenter", () => {
  const tags = document.querySelectorAll(".tag_item");
  tags.forEach((icon) => closeAction(icon)
  );
});

function closeAction(element) {
  const actionable_tag = element.textContent;
  const closeIcon = element.querySelector(".fa");
  closeIcon.addEventListener("click", () => {
    tags = tags.filter((tag) => tag !== actionable_tag.trim());
    setTags();
  });
}

function setTags() {
  selectedTags.innerHTML = tags
    .map((tag) => {
      return `
        <span class="tag_item">${tag} <i class="fa fa-times" aria-hidden="true"></i></span>
      `;
    })
    .join("");
}
