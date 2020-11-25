<template>
  <div>
    <div class="signup-form-title">
      <span> 담당자 정보</span>
      <span>(*실제 샵을 운영하시는 분)</span>
    </div>
    <a-form-item>
      <a-input
        type="tel"
        v-decorator="[
          'owner_number',
          {
            rules: [
              {
                required: true,
                message: '올바른 정보를 입력해주세요.',
              },
              {
                pattern: /^(?=.*[-]).{11,13}$/,
                message: '번호 사이에 - 을 넣어주세요.',
              },
              {
                pattern: /^(?=.*[0-9]).{11,13}$/,
                message: '전화번호 형식으로 입력해주세요.',
              },
            ],
          },
        ]"
        placeholder="핸드폰번호"
      >
        <a-icon slot="prefix" type="phone" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <div class="signup-form-extra">
      <a-icon type="info-circle" theme="filled" />
      <span
        >입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를
        기입해주세요.</span
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "Signup-owner",
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.signup-form {
  .ant-form {
    &-item {
      margin-bottom: 8px;
    }
    /* &-explain */
  }

  &-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 5px;
    > span:last-child {
      font-size: 14px;
      font-weight: 400;
      color: rgb(30, 144, 255);
    }
  }

  &-extra {
    @include flexSet("flex-start", "center");
    margin: -10px 0 50px;
    font-size: 12px;
    font-weight: 600;
    color: rgb(30, 144, 255);

    > span {
      margin-left: 5px;
    }
  }
}
</style>
