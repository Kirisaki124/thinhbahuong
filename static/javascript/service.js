
$(document).ready(function() {
  var total_package = 0;
  var package_1 = 0;
  var package_2 = 0;
  var package_3 = 0;
  function cart () {
    $("#cart").html(total_package);
  };

  $("#add_cart_1").click(function(event){
    total_package +=1;
    package_1 +=1;
    $("#add_cart_1_input").val(package_1);
    cart();
  });
  $("#add_cart_2").click(function(event){
    total_package +=1;
    package_2 +=1;
    $("#add_cart_2_input").val(package_2);
    cart();
  });
  $("#add_cart_3").click(function(event){
    total_package +=1;
    package_3 +=1;
    $("#add_cart_3_input").val(package_3);
    cart();

  });
});
