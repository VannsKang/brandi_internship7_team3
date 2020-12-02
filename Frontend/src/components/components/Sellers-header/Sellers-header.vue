<template>
  <div>
    <a-page-header
      class="sellers-header"
      :title="header.title"
      :sub-title="header.sub_title"
    />
    <a-breadcrumb class="sellers-breadcrumb" separator=">">
      <a-breadcrumb-item>
        <a-icon type="home" theme="filled" />
      </a-breadcrumb-item>
      <a-breadcrumb-item
        v-for="(crumb, index) in header.breadcrumb"
        :key="index"
      >
        <span>{{ crumb }}</span>
      </a-breadcrumb-item>
    </a-breadcrumb>
  </div>
</template>

<script>
export default {
  name: "Seller-header",

  props: {
    header: {
      type: Object,
      required: true,
    },
  },
};
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

    > i {
      margin-right: 10px;
    }
  }
}
</style>
