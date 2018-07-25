window.onload = function (){
  $(".display div").hide();
  $(".display div").first().show();

  $("#page-1-1").click(function(){
  $(".button").click(function(){
      $(".display div").hide();
      $(".display .page-2").first().show();
    });

  $("#page-2-1").click(function(){
      $(".display div").hide();
      $(".display .page-3").first().show();
  });

  $("#page-3-1").click(function(){
      $(".display div").hide();
      $(".display .page-4").first().show();
    });

  $("#page-4-1").click(function(){
      $(".display div").hide();
      $(".display .page-5").first().show();
    });

  $("#page-5-1").click(function(){
      $(".display div").hide();
      $(".display .page-6").first().show();
    });

  $("#page-6-1").click(function(){
      $(".display div").hide();
      $(".display .page-7").first().show();
    });

}
