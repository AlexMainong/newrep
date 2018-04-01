function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});
$(document).ready(function(){
     function updateText(btn, newCount, verb){
     btn.text(newCount + " " + verb)
     btn.attr("data-likes", newCount)
 }
 $(".like-btn").click(function(e){
   e.preventDefault()
   var this_ = $(this)
   var likeUrl = this_.attr("data-href")
   var likeCount = parseInt(this_.attr("data-likes")) | 0
   var addLike = likeCount + 1
   var removeLike = likeCount - 1
   if (likeUrl){
      $.ajax({
       url: likeUrl,
       method: "GET",
       data: {},
       success: function(data){
         console.log(data)
         var newLikes;
         if (data.liked){
             updateText(this_, addLike, "Мне нравится")
         } else {
             updateText(this_, removeLike, "Мне нравится")
         }
       }, error: function(error){
         console.log(error)
         console.log("error")
       }
     })
   }

 })
})
$(document).ready(function(){
})
