<template>
  <a-layout class="Page403">
    <a-result status="403" title="403" sub-title="잘못된 접근입니다!">
      <template #extra>
        <a-button type="primary" @click="backHome" class="backHome">
          로그인 화면으로
        </a-button>
      </template>
    </a-result>
  </a-layout>
</template>

<script>
export default {
  name: "Page-403",

  methods: {
    backHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style src="./Page-403.scss" lang="scss" scoped />
