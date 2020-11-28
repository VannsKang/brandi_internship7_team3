<template>
  <div>
    <a-page-header
      class="sellers-header"
      title="셀러 계정 관리"
      sub-title="셀러 회원 목록 / 관리"
    />
    <a-breadcrumb class="sellers-breadcrumb" separator=">">
      <a-breadcrumb-item href="">
        <a-icon type="home" theme="filled" />
        <span>회원 관리</span>
      </a-breadcrumb-item>
      <a-breadcrumb-item href="">
        <span>셀러 계정 관리 </span>
      </a-breadcrumb-item>
      <a-breadcrumb-item>
        셀러 회원 리스트
      </a-breadcrumb-item>
    </a-breadcrumb>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.sellers {
  &-header {
    font-size: 26px !important;
    height: 68px;
  }
  &-breadcrumb {
    width: 100%;
    background: #e8e8e8;
    padding: 7px 0 7px 25px;
    font-size: 13px;
  }
}
</style>
