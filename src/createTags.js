const length = document.getElementsByClassName("js-navigation-open Link--primary").length;
let tags = []
for(var i = 0; i < length; i++) {
  var tag = document.getElementsByClassName("js-navigation-open Link--primary")[i].getAttribute("title").split(".")[0];
    tags.push(tag);
}
result = new Set();
for (tag of tags) {
    // Convert tag from camel case to kebab case
    const kebabCaseTag = tag.replace(/([a-z])([A-Z])/g, "$1-$2").toLowerCase();

    result.add(kebabCaseTag);
}
console.log(Array.from(result).join(", "));
  