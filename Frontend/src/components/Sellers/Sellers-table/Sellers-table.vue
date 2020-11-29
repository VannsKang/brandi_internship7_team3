<template>
  <div class="sellers-content-main-table">
    <table>
      <!-- SECTION table header -->

      <thead>
        <tr>
          <th>
            <div>
              <a-checkbox
                :indeterminate="indeterminate"
                :checked="checkAll"
                @change="onCheckAllChange"
              />
            </div>
          </th>
          <th v-for="column in columns" :key="column.dataIndex">
            <div>
              {{ column.title }}
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <!-- SECTION search row -->

        <tr>
          <td />

          <td v-for="column in columns.slice(0, 5)" :key="column.dataIndex">
            <div>
              <a-input
                :id="column.dataIndex"
                v-model.lazy="searchData[column.dataIndex]"
                :value="input_value"
                @keyup.enter="searchInput"
              />
            </div>
          </td>

          <!-- STUB seller status -->
          <td>
            <div>
              <a-select
                :default-value="select_value"
                style="width: 80px"
                @change="searchSellerDropdown"
              >
                <a-select-option
                  v-for="stat in seller_status"
                  :key="stat.name"
                  name="seller_status"
                  :value="stat.seller_status_id"
                >
                  {{ stat.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>
          <!-- STUB email, phoneNumber -->
          <td v-for="column in columns.slice(6, 8)" :key="column.dataIndex">
            <div>
              <a-input
                :id="column.dataIndex"
                v-model.lazy="searchData[column.dataIndex]"
                :value="input_value"
                @keyup.enter="searchInput"
              />
            </div>
          </td>

          <!-- STUB seller attribute -->
          <td>
            <div>
              <a-select
                :default-value="select_value"
                style="width: 100px"
                @change="searchSellerDropdown"
              >
                <a-select-option
                  v-for="attribute in seller_attribute_id"
                  :key="attribute.name"
                  name="seller_attribute_id"
                  :value="attribute.seller_attribute_id"
                >
                  {{ attribute.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>

          <!-- STUB calendar -->
          <td>
            <div>
              <a-date-picker
                placeholder="From"
                @change="
                  (date, dateString) =>
                    onDateChange('start_time', data, dateString)
                "
              />
              <a-date-picker
                placeholder="to"
                @change="
                  (date, dateString) =>
                    onDateChange('end_time', data, dateString)
                "
              />
            </div>
          </td>

          <td>
            <div>
              <a-button type="primary" @click="submitSearch">
                <a-icon type="search" />
                <span>Search</span>
              </a-button>
              <a-button type="primary" @click="resetSearch">
                <a-icon type="close" />
                <span>Reset</span>
              </a-button>
            </div>
          </td>
        </tr>

        <!-- SECTION datarow -->

        <tr v-for="item in data" :key="item.id">
          <td>
            <div>
              <a-checkbox
                :id="item.id.toString()"
                class="listItems"
                @change="changeEachCheckBox"
              />
            </div>
          </td>

          <td>
            <div>
              {{ item.id }}
            </div>
          </td>

          <td>
            <div :id="item.id" @click="moveSellerDetails">
              {{ item.seller_id }}
            </div>
          </td>

          <template
            v-for="(val, name) in [
              item.eng_name,
              item.kor_name,
              item.owner_name,
              item.seller_status,
              item.phone_number,
              item.email,
              item.seller_attribute,
              item.created_at,
            ]"
          >
            <td :key="name">
              <div>
                {{ val }}
              </div>
            </td>
          </template>

          <td>
            <span>
              <a-button
                v-for="btn in item.seller_actions"
                :key="btn.id"
                :data-id="item.id"
                :data-btn="btn.id"
                :style="confirmBtnColor(+btn.id)"
                @click="handleActions"
              >
                {{ btn.name }}
              </a-button>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SellersTable",

  components: {},

  props: {
    data: {
      type: Array,
      required: true,
    },
    columns: {
      type: Array,
      required: true,
    },
    searchInput: {
      type: Function,
      required: true,
    },
    searchSellerDropdown: {
      type: Function,
      required: true,
    },
    onDateChange: {
      type: Function,
      required: true,
    },
    searchData: {
      type: Object,
      required: true,
    },
    submitSearch: {
      type: Function,
      required: true,
    },
    resetSearch: {
      type: Function,
      required: true,
    },
    handleActions: {
      type: Function,
      required: true,
    },
  },

  data() {
    return {
      // ANCHOR for list control
      indeterminate: false,
      checkAll: false,
      plainOptions: [],
      checkedList: [],

      // ANCHOR Pagination
      page: {
        number: 1,
      },

      // ANCHOR for input items
    };
  },

  methods: {
    // ANCHOR checkbox control
    changeEachCheckBox(e) {
      const { checked, id } = e.target;

      if (checked) {
        this.checkedList = [...this.checkedList, +id];
      } else {
        this.checkedList = this.checkedList.filter(
          (checkItem) => checkItem !== +id
        );
      }

      this.indeterminate =
        !!this.checkedList.length &&
        this.checkedList.length < this.plainOptions.length;
      this.checkAll = this.checkedList.length === this.plainOptions.length;
    },

    onCheckAllChange(e) {
      console.log(e.target);
      const { checked } = e.target;

      const eachInput = document.querySelectorAll(".listItems");
      eachInput.forEach((item) =>
        checked
          ? item.childNodes[0].classList.add("ant-checkbox-checked")
          : item.childNodes[0].classList.remove("ant-checkbox-checked")
      );

      Object.assign(this, {
        checkedList: e.target.checked ? this.plainOptions : [],
        indeterminate: false,
        checkAll: checked,
      });
    },

    getCheckboxId() {
      const { data } = this.$props;
      const allDataId = data.map((item) => item.id);
      this.plainOptions = allDataId;
    },

    // TODO move to seller detail
    moveSellerDetails(e) {
      const { id } = e.target;
      this.$router.push(`/main/seller/info/${id}`);
    },

    // SECTION btn styler

    confirmBtnColor(btn) {
      if (btn === 3 || btn === 6)
        return {
          background: `#f0ad4e`,
          border: "1px solid #eea236",
        };

      if (btn === 1 || btn === 4)
        return {
          background: `#5bc0de`,
          border: "1px solid #46b8da",
        };

      if (btn === 5 || btn === 2 || btn === 7)
        return {
          background: `#d9534f`,
          border: `1px solid #d43f3a`,
        };
    },
  },

  computed: {
    ...mapState({
      seller_attribute_id: ({ sellers }) => sellers.seller_attribute_id,
      seller_status: ({ sellers }) => sellers.seller_status,
      input_value: ({ sellers }) => sellers.input_value,
      select_value: ({ sellers }) => sellers.select_value,
    }),
  },

  // SECTION Life cycle
  beforeUpdate() {
    this.getCheckboxId();
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.sellers-content-main-table {
  margin: 0 10px;
  border: 1px solid #ddd;
  overflow-x: scroll;

  > table {
    min-width: 1500px;
    border-collapse: separate;
    /* margin-bottom: 5px; */
    > thead {
      height: 36px;
      background: #eee;
      font-weight: 700;
      > tr {
        > th {
          border-right: 1px solid #ddd;
          padding: 5px 5px;
          > div {
            width: 100%;
          }
          &:nth-child(1) {
            width: 40px;
            > div {
              @include flexSet("center", "center");
            }
          }
          &:nth-child(2) {
            width: 60px;
          }
          &:nth-child(3) {
            width: 118px;
          }
          &:nth-child(4) {
            width: 115px;
          }
          &:nth-child(5) {
            width: 140px;
          }
          &:nth-child(6) {
            width: 96px;
          }
          &:nth-child(7) {
            width: 65px;
          }
          &:nth-child(8) {
            width: 137px;
          }
          &:nth-child(9) {
            width: 105px;
          }
          &:nth-child(10) {
            width: 85px;
          }
          &:nth-child(11) {
            width: 179px;
          }
          &:nth-child(12) {
            width: 271px;
            border-right: 0;
          }
        }
      }
    }
    tbody {
      tr {
        height: 38px;
        &:nth-child(even) {
          background: #f5f5f5;
        }

        &:hover {
          background: darken($color: #f5f5f5, $amount: 2%);
        }

        &:first-child {
          &:hover {
            background: none;
          }

          td {
            padding: 10px;
            > div {
              @include flexSet(null, "flex-start", "column");

              > button {
                padding: 5px 10px;
                font-size: 12px;

                > span {
                  margin-left: 3px;
                }

                &:first-child {
                  background: #f0ad4e;
                  border-color: #eea236;
                  margin-bottom: 5px;

                  &:hover {
                    background: darken(#f0ad4e, 10%);
                  }
                }

                &:last-child {
                  background: #d9534f;
                  border-color: #d43f3a;

                  &:hover {
                    background: darken(#d9534f, 10%);
                  }
                }
              }
            }
          }
        }

        td {
          font-size: 13px;
          border-right: 1px solid #ddd;
          border-top: 1px solid #ddd;
          padding: 5px 10px;

          &:nth-child(3) {
            color: #0d638f;
            cursor: pointer;
            &:hover {
              text-decoration: underline;
            }
            div {
            }
          }
          &:nth-child(11) {
            > div {
              > span {
                &:last-child {
                  margin-top: 5px;
                }
              }
            }
          }
          &:last-child {
            border-right: 0;
            > span {
              button {
                padding: 3px;
                font-size: 12px;
                margin-right: 5px;
                line-height: 12px;
                height: 25px;
                color: #fff;
                &:last-child {
                  margin-right: 0;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>
