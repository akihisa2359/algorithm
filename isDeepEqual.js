// https://www.syncfusion.com/blogs/post/5-different-ways-to-deep-compare-javascript-objects.aspx

const isObject = (object) => {
  return object !== null && typeof object === "object";
};

const isDeepEqual = (object1, object2) => {
  const objectKeys1 = Object.keys(object1);
  const objectKeys2 = Object.keys(object2);
  if (objectKeys1.length !== objectKeys2.length) return false;

  for (const key of objectKeys1) {
    value1 = object1[key];
    value2 = object2[key];
    const areObjects = isObject(value1) && isObject(value2);
    if (
      (areObjects && !isDeepEqual(value1, value2)) ||
      (!areObjects && value1 !== value2)
    ) {
      return false;
    }
  }

  return true;
};

const obj1 = { a: 1, b: { b1: "b1", b2: "b2" }, c: [1, 2, 3] };
const obj2 = { a: 1, b: { b1: "b1", b2: "b2" }, c: [1, 2, 3] };

console.log(isDeepEqual(obj1, obj2));
