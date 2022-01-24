let btnClear = document.querySelector(".btn-danger");
let inputs = document.querySelectorAll("input");

btnClear.addEventListener("click", () => {
    inputs.forEach((input) => (input.value = ""));
});
