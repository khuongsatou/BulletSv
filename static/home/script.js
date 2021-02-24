function requestNotify() {
  $.ajax({
    url: "/api/notify",
    type: "POST",
    data: JSON.stringify({}),
    success: function (response) {
      console.log(response);
    },
    error: function (xhr, error, response) {
      console.log(response);
    },
    cache: false,
    contentType: false,
    processData: false,
  });
}

function AjaxCallAxis() {
  var now = new Date();
  let futureDay = new Date(
    new Date().setMinutes(
      now.getMinutes(),
      now.getSeconds() + 15,
      now.getMilliseconds()
    )
  );

  var x = setInterval(function () {
    var nowCurrent = new Date();
    if (Number(nowCurrent.getTime()) >= Number(futureDay.getTime())) {
      requestNotify();
      clearInterval(x);
    }
  }, 1000);
  console.log("run...");
}
