<template>
  <div class="Singup-basic">
    <div class="signup-form-title">
      가입 정보
    </div>
    <a-form-item>
      <a-input
        v-decorator="[
          'user_id',
          {
            rules: [
              { required: true, message: '필수 입력항목입니다.' },
              { min: 5, message: '아이디의 최소 길이는 5글자입니다.' },
              {
                pattern: /^([A-Za-z0-9])([A-Za-z0-9_-]){4,19}$/,
                message:
                  '아이디는 5~20글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.',
              },
            ],
          },
        ]"
        placeholder="아이디"
      >
        <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item has-feedback>
      <a-input
        v-decorator="[
          'password',
          {
            rules: [
              {
                validator: validateToNextPassword,
              },
              {
                pattern: /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[~!@#$%^&*()\-_=+,.<>/?;:[{}\]\\|]).{8,20}$/,
                message:
                  '비밀번호는 8~20글자의 영문대소문자, 숫자, 특수문자를 조합해야 합니다.',
              },
            ],
          },
        ]"
        type="password"
        placeholder="비밀번호"
        autocomplete
      >
        <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item has-feedback>
      <a-input
        v-decorator="[
          'confirm_password',
          {
            rules: [
              {
                validator: compareToFirstPassword,
                message: '비밀번호가 일치하지 않습니다.',
              },
            ],
          },
        ]"
        type="password"
        placeholder="비밀번호 재입력"
        autocomplete
        @blur="confirmPasswordBlur"
      >
        <a-icon slot="prefix" type="check" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
  </div>
</template>

<script>
export default {
  name: "Singup-basic",

  props: {
    form: {
      type: Object,
    },
  },

  data() {
    return {
      confirmDirty: false,
    };
  },

  methods: {
    confirmPasswordBlur(e) {
      const { value } = e.target;
      this.confirmDirty = this.confirmDirty || !!value;
    },

    validateToNextPassword(rule, value, callback) {
      value &&
        this.confirmDirty &&
        this.form.validateFields(["confirm"], { force: true });
      callback();
    },

    compareToFirstPassword(rule, value, callback) {
      value && value !== this.form.getFieldValue("password")
        ? callback("not matched!")
        : callback();
    },
  },
};
</script>

<style src="./Singup-basic.scss" lang="scss" scoped />
