/*
Generates a node for a singly linked list
parameters:
  val: a numerical value
private variables/functions:
  none:
public properties/methods:
  val: val;
  next: // another Node or null
  passThis: a function that passes a console log of this and self.
************** END **********   */
var Node = function(val){
  this.val = val;
  this.next = null;
}
Node.prototype.passThis = function(custom_return){
  console.log(this, "this");
  console.log(this.self, "self");
  console.log(custom_return, "My Return");
  return custom_return;
}
// ****************** END OF NODE ******************

var SingleList= function(){
  this.head = null;
}

SingleList.prototype.add = function (val) {
  if (!this.head){
    this.head = new Node(val);
    return this;
  }
  var current = this.head;
  while(current.next){
    current = current.next;
  }
  current.next = new Node(val);
  return this;
};

SingleList.prototype.dequeue = function (callback) {
  var eliminatedNode = this.head;
  this.head = this.head.next;
  eliminatedNode.next = null;
  if (typeof(callback)=='function'){
    callback(eliminatedNode);
  }
  //console.log(this.head); optional
  return this;
};

// ************************ END OF LIST ************************
sList = new SingleList();
sList.add(1).add(2).add(3).add(4).head.next.passThis(sList).dequeue(
  function callback(myNode){
    console.log(myNode.val, "CHAINING INSANITY!");
  })
  .dequeue(
    function anotherCallback(myNode){
      console.log("******************************");
      console.log('Seriously, Stop!', myNode);
    });