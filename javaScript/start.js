window.onload = function (){
  $(".display div").hide();
  $(".display div").first().show();

  $("#page-1-1").click(function(){
      $(".display div").hide();
      $(".display .page-2").first().show();
      // pagecount = 1;
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
    $("#page-6-2").click(function(){
        $(".display div").hide();
        $(".display .page-71").first().show();
        });
  $("#page-7-1").click(function(){
      $(".display div").hide();
      $(".display .page-8").first().show();
      });
  $("#page-8-1").click(function(){
      $(".display div").hide();
      $(".display .page-9").first().show();
      });
}
