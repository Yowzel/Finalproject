
function hello (number) {
  if (number<=0) {
    $(".display div").hide();
    $(".display .page-1").first().show();
  } else {
    $(".display div").hide();
    $(".display .page-" + number).first().show();
  }

}

window.onload = function (){


  // $(".display div").hide();
  // $(".display div").first().show();

  $("#page-1-1").click(function(){
      $(".display div").hide();
      $(".display .page-2").first().show();
      // pagecount = 1;
    });

  $("#page-2-1").click(function(){
      $(".display div").hide();
      $(".display .page-3").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '3'
        }
      })
  });

  $("#page-3-1").click(function(){
      $(".display div").hide();
      $(".display .page-4").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '4'
        }
      })
    });

  $("#page-4-1").click(function(){
      $(".display div").hide();
      $(".display .page-5").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '5'
        }
      })
    });

  $("#page-5-1").click(function(){
      $(".display div").hide();
      $(".display .page-6").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '6'
        }
      })
    });

  $("#page-6-1").click(function(){
      $(".display div").hide();
      $(".display .page-7").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '7'
        }
      })
    });
  $("#page-6-2").click(function(){
      $(".display div").hide();
      $(".display .page-71").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '71'
        }
      })
    });
  $("#page-7-1").click(function(){
      $(".display div").hide();
      $(".display .page-9").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '9'
        }
      })
      });
  $("#page-7-1-1").click(function(){
      $(".display div").hide();
      $(".display .page-9").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '9'
        }
      })
      });
  $("#page-8-2").click(function(){
      $(".display div").hide();
      $(".display .page-8").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '8'
        }
      })
      });
  $("#page-4-2").click(function(){
      $(".display div").hide();
      $(".display .page-11").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '11'
        }
      })
      });
  $("#page-4-2-2").click(function(){
      $(".display div").hide();
      $(".display .page-11").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '11'
        }
      })
      });
  $("#page-4-2-2-2").click(function(){
      $(".display div").hide();
      $(".display .page-11").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '11'
        }
      })
      });
  $("#page-11-1").click(function(){
      $(".display div").hide();
      $(".display .page-12").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '12'
        }
      })
      });
  $("#page-81-1").click(function(){
      $(".display div").hide();
      $(".display .page-711").first().show();
      $.post({
        url: '/saved',
        data: {
          progress: '711'
        }
      })
      });
}
