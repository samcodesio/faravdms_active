let btnClear = document.querySelector(".btn-danger");
let inputs = document.querySelectorAll("input");

btnClear.addEventListener("click", () => {
  inputs.forEach((input) => (input.value = ""));
});

let twocat = document.querySelector("#twocat");
let onecat = document.querySelector("#onecat");
let catsubcat2 = document.querySelector("#catsubcat2");

// CATEGORY 1 SUBCATEGORY 1
const catdata = document.getElementById("category");
const subcatdata = document.getElementById("subcategory");
const defaultText = document.getElementById("defaultText");

// CATEGORY 2 SUBCATEGORY 2
const catdata2 = document.getElementById("category2");
const subcatdata2 = document.getElementById("subcategory2");
const defaultText2 = document.getElementById("defaultText2");

// catsubcat2.style.display = "none";
twocat.addEventListener("change", function () {
  if (this.checked) {
    // catsubcat2.style.display = "block";
    catsubcat2.classList.remove("idle");
    // twocat.value = "Yes"
  } else {
    catsubcat2.classList.add("idle");
    // twocat.value = "No"
  }
});

//--------------populating values for CATEGORY1 via JSOn--------------
$.ajax({
  type: "GET",
  url: "/cat_json",
  success: function (response) {
    console.log(response.data);
    const catData = response.data;
    catData.map((item) => {
      const option = document.createElement("option");
      option.textContent = item.category_name;
      option.setAttribute("class", "item");
      option.setAttribute("data-value", item.id);
      catdata.appendChild(option);
    });
  },
  error: function (error) {
    console.log(error);
  },
});

catdata.addEventListener("change", (e) => {
  console.log(e.target.value);
  const selectedCat = e.target.value;
  subcatdata.innerHTML = "";
  defaultText.textContent = "--Select Sub Category--";

  $.ajax({
    type: "GET",
    url: `subcat_json/${selectedCat}`,
    success: function (response) {
      console.log(response.data);
      const subcatData = response.data;
      subcatData.map((item) => {
        const option = document.createElement("option");
        option.textContent = item.sub_category_name;
        option.setAttribute("class", "item");
        option.setAttribute("data-value", item.id);
        subcatdata.appendChild(option);
      });
    },
    error: function (error) {
      console.log("not running",error);
    },
  });
});

// CATEGORY 2 SUBCATEGORY 2

$.ajax({
  type: "GET",
  url: "/cat_json2",
  success: function (response) {
    console.log(response.data);
    const catData2 = response.data;
    catData2.map((item) => {
      const option = document.createElement("option");
      option.textContent = item.category_name;
      option.setAttribute("class", "item");
      option.setAttribute("data-value", item.id);
      catdata2.appendChild(option);
    });
  },
  error: function (error) {
    console.log(error);
  },
});

catdata2.addEventListener("change", (e) => {
  console.log(e.target.value);
  const selectedCat = e.target.value;

  subcatdata2.innerHTML = "";
  defaultText.textContent = "--Select Sub Category--";

  $.ajax({
    type: "GET",
    url: `subcat_json2/${selectedCat}`,
    success: function (response) {
      console.log(response.data);
      const subcatData2 = response.data;
      subcatData2.map((item) => {
        const option = document.createElement("option");
        option.textContent = item.sub_category_name;
        option.setAttribute("class", "item");
        option.setAttribute("data-value", item.id);
        subcatdata2.appendChild(option);
      });
    },
    error: function (error) {
      console.log(error);
    },
  });
});

$(document).ready(function () {
  $(".js-example-basic-multiple").select2();
});

//

// $.ajax({
//   type: 'GET',
//   url: '/displaydata/14/',
//   success: function(response){
//     console.log(response.data)

//   },
//   error: function(error){
//     console.log(error)
//   }
// })

// const id = document.getElementById('form-id').value()
// console.log(id)

// ********* DATA TABLES Buttons ************ //
$(document).ready(function () {
  $("#datatablesSimple").DataTable({
    dom: "Bfrtip",
    buttons: ["copy", "csv", "excel", "pdf", "print"],
  });
});
