<template>
  <section class="main-footer">
    <div>
      <span>
        | 상호 : (주)브랜디 | 주소 : (06223) 서울특별시 강남구 테헤란로 32길 26
        청송빌딩 | 사업자등록번호 : 220-88-93187 | 통신판매업신고 :
        2016-서울강남-00359호 | 이메일 : help@brandi.co.kr
      </span>
      <span>2020 © brandi inc.</span>
    </div>
  </section>
</template>

<script>
export default {
  name: "Main-footer",
};
</script>

<style lang="scss" scoped>
@import "../../../styles.scss";

.main-footer {
  width: 100%;
  background: $nav-side-color;
  padding: 10px 20px 5px;
  font-size: 12px;
  color: #999ba2;
  div {
    @include flexSet("center", "flex-start", "column");
  }
}
</style>
