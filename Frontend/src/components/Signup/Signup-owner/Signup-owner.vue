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
      <span>
        입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를
        기입해주세요.
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupOwner",
};
</script>

<style src="./Singup-owner.scss" lang="scss" scoped />
