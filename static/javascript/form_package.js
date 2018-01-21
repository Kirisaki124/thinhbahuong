$(document).ready(function() {
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
    $("#add_cart_2_input").val(package_2);
    cart();

  });
});
