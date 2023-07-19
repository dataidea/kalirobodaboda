const form = document.querySelector("form");
const labels = document.querySelectorAll("label");
const inputs = document.querySelectorAll("input");
const p_tags = document.querySelectorAll("p");

// Design inputs
inputs.forEach((input) => {
  input.classList.add(
    "border",
    "rounded",
    "p-2",
    "block",
    "w-full",
    "dark:text-gray-600"
  );
});

// Design label elements
labels.forEach((label) => {
  label.classList.add("py-3");
});

// Design paragraph tags, django forms are grouped in templates
p_tags.forEach((tag) => {
  tag.classList.add("py-2");
});

// Design form inputs
form.classList.add("dark:text-gray-200");
form.gender.classList.add("p-2", "dark:text-gray-600");
form.first_name.placeholder = "John";
form.last_name.placeholder = "Doe";
form.username.placeholder = "johndoe";
form.email.placeholder = "johndoe@gmail.com";
