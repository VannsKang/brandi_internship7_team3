<template>
  <div class="sellers-content-main-pagination">
    <span>Page</span>
    <div class="sellers-content-main-pagination-button">
      <a-button
        data-id="minus"
        @click="controlPages"
        :disabled="page_number <= 1"
      >
        <a-icon type="left" />
      </a-button>
      <!-- SECTION pagenation number -->
      <a-input-number v-model="page_number" />

      <a-button
        data-id="plus"
        @click="controlPages"
        :disabled="page_number >= Math.ceil(seller_count / currentPagination)"
      >
        <a-icon type="right" />
      </a-button>
    </div>
    <span>of {{ Math.ceil(seller_count / currentPagination) }} | View</span>
    <a-select
      class="sellers-content-main-pagination-group"
      :value="currentPagination"
      @change="controlPagesDrop"
    >
      <a-select-option
        v-for="(page, idx) in pageControl"
        :value="page"
        :key="idx"
      >
        {{ page }}
      </a-select-option>
    </a-select>
    <span>records | Found total {{ seller_count }} records</span>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Sellers-pagination",

  props: {
    controlPages: {
      type: Function,
      required: true,
    },

    controlPagesDrop: {
      type: Function,
      required: true,
    },

    page_number: {
      type: Number,
      required: true,
    },

    seller_count: {
      type: Number,
      required: true,
    },

    currentPagination: {
      type: Number,
      required: true,
    },
  },

  data() {
    return {};
  },

  methods: {},

  computed: {
    ...mapState({
      pageControl: ({ sellers }) => sellers.pageControl,
    }),
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.sellers-content-main-pagination {
  @include flexSet("flex-start", "center");
  margin: 10px;
  color: #111;

  &-button {
    width: 110px;
    margin: 0 10px;
    @include flexSet("space-between", "center");

    > button {
      padding: 8px;
      font-size: 9px;
      @include flexSet("center", "center");
    }

    .ant-input-number {
      width: 45px;
    }
  }

  &-group {
    margin: 0 10px;
    width: 80px;
  }
}
</style>
