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

<style src="./Sellers-header.scss" lang="scss" scoped />
