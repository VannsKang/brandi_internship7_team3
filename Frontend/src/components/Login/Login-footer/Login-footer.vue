<template>
  <a-layout-footer class="login-footer">
    <div>
      <div>
        <span>
          회사명 : (주)브랜디 | 주소 : (06223) 서울특별시 강남구 테헤란로 32길
          26 청송빌딩 | 사업자등록번호 : 220-88-93187 I 통신판매업신고 :
          2016-서울강남-00359호
        </span>
        <span>
          이메일 : help@brandi.co.kr | 2020 © brandi inc.
        </span>
      </div>
      <div>
        <span>이용약관</span> |
        <span>개인정보처리방침</span>
      </div>
    </div>
  </a-layout-footer>
</template>

<script>
export default {
  name: "Login-footer",
};
</script>

<style lang="scss" scoped>
@import "../../../styles.scss";
.login-footer {
  text-align: left;
  height: 107px;
  padding: 20px 0;
  background: #202020;
  color: #999;
  @include flexSet("center", "center", column);

  > div {
    div {
      margin: 0 60px;
      font-size: 11px;
      letter-spacing: -0.5px;
      line-height: 1.8;

      &:first-child {
        span {
          display: block;
        }
      }

      &:last-child {
        font-size: 12px;
        margin-top: 10px;
        color: #fff;

        span {
          &:last-child {
            font-weight: 700;
            text-decoration: underline;
          }
        }
      }
    }
  }
}
</style>
