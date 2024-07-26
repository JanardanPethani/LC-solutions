// Hash table, Linked List

// Definition for a _Node.
function _Node(val, next, random) {
  this.val = val;
  this.next = next;
  this.random = random;
}

const n2 = new _Node(2, null, 1);
const n1 = new _Node(1, n2, 1);

const mapperHash = new Map();

var copyRandomList = function (head) {
  if (!head) return null;

  // traverse through all the nodes, clone and save in hash
  let newNode = new _Node(head.val, null, null);
  mapperHash.set(head, newNode);

  if (head.next === null) {
    if (head.random) {
      newNode.random = mapperHash.get(head.random);
    }
    return mapperHash.get(head);
  }

  if (head.next) {
    newNode.next = copyRandomList(head.next);
  }

  if (head.random) {
    newNode.random = mapperHash.get(head.random);
  }

  return mapperHash.get(head);
};

// --- extra code below ---
copyRandomList(n1);
const nodeList = [];
for (const node of mapperHash.values()) {
  nodeList.push(node);
}
console.log(nodeList);
