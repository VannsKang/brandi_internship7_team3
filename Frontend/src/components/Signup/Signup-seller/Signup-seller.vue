<template>
  <div>
    <div class="signup-form-title">셀러 정보</div>

    <a-form-item>
      <a-radio-group v-decorator="['seller_attribute_id']">
        <a-radio
          v-for="seller in seller_attribute_id"
          :value="seller.seller_attribute_id"
          :key="seller.seller_attribute_id"
        >
          {{ seller.name }}
        </a-radio>
      </a-radio-group>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'name',
          {
            rules: [
              { required: true, message: '필수 입력항목입니다.' },
              { min: 1, message: '셀러명의 최소 길이는 1글자입니다.' },
            ],
          },
        ]"
        placeholder="셀러명 (상호)"
      >
        <a-icon slot="prefix" type="font-size" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'eng_name',
          {
            rules: [
              { required: true, message: '필수 입력항목입니다.' },
              {
                min: 1,
                message: '영문 상호명의 최소 길이는 1글자입니다.',
              },
              {
                pattern: /^([A-Za-z0-9\uac00-\ud7af])+(\1?)$/,
                message:
                  '영문 상호명은 1글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.',
              },
            ],
          },
        ]"
        placeholder="영문 상호명"
      >
        <a-icon slot="prefix" type="font-size" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'cs_number',
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
        placeholder="고객센터 전화번호"
      >
        <a-icon slot="prefix" type="phone" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Signup-seller",

  data() {
    return {};
  },

  computed: {
    ...mapState({
      seller_attribute_id: ({ sellers }) => sellers.seller_attribute_id,
    }),
  },

  methods: {
    ...mapActions("sellers", ["updateSellerAttributeAction"]),
  },

  // SECTION lifecycle
  mounted() {
    this.updateSellerAttributeAction();
  },
};
</script>

<style src="./Signup-seller.scss" lang="scss" scoped />
