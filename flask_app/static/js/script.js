$("#slideshow > div:gt(0)").hide();

setInterval(function() { 
  $('#slideshow > div:first')
  .fadeOut(1000)
  .next()
  .fadeIn(1000)
  .end()
  .appendTo('#slideshow');
}, 3000);


$('#urlsubmit').on('click', function(){
$("div#media").append( "<h2><a href='"+$('#url').text()+"id='"+$("#name").text()+"'/></h2>");
});

$("#playvideo").click(function(){
  $("#video1")[0].src += "?autoplay=1";
  });


function togglePopup() {
  document.getElementById("popup-1")
  .classList.toggle("active");
}

function myPopup(myURL, title, myWidth, myHeight) {
  var left = (screen.width - myWidth) / 2;
  var top = (screen.height - myHeight) / 4;
  var myWindow = window.open(myURL, title, 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width=' + myWidth + ', height=' + myHeight + ', top=' + top + ', left=' + left);
}










// $.getJSON("https://api.openweathermap.org/data/2.5/weather?q=Puyallup&units=imperial&appid=a33dfaf0df1403f15022a2950364521c", 
//   function (data) {
//     console.log(data);

//     var icon = 
//       "https://openweathermap.org/img/w/" + data.weather[0].icon + ".png";
//     var temp = Math.floor(data.main.temp);
//     var weather = data.weather[0].main;

//     $(".icon").attr("src", icon);
//     $(".weather").append(weather);
//     $(".temp").append(temp);
//   }
// );







