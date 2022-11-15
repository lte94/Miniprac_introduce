// totop
const toTopEl = document.querySelector("#to-top");

window.addEventListener(
  "scroll",
  _.throttle(function () {
    console.log(window.scrollY);
    if (window.scrollY > 500) {
      // gsap.to(요소, 지속시간 , 옵션 )
      //버튼 보이기
      gsap.to(toTopEl, 0.2, {
        x: 0,
      });
    } else {
      //버튼 숨기기
      gsap.to(toTopEl, 0.2, {
        x: 100,
      });
    }
  }, 300)
);
toTopEl.addEventListener("click", function () {
  gsap.to(window, 0.7, {
    scrollTo: 0,
  });
});

$(".jaehyun").click(function () {
  $.ajax({
    type: "GET",
    url: "/user/1",
    success: function (response) {
      console.log(JSON.stringify(response));
    },
  });
});

// 방명록

// const commentBtn = document.querySelector("#button-addon2");

// commentBtn.addEventListener("click", save_commnet);

// function save_commnet() {
//   $.ajax({
//     type: "POST",
//     url: "user/1",
//     data: { sample_give: "데이터전송" },
//     success: function (response) {
//       alert(response["msg"]);
//     },
//   });
// }
