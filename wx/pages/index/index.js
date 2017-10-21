//index.js
var util = require('../../utils/util.js');

//获取应用实例
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 材质
    material_index: 0,
    material_array: ['201', '304'],

    // 颜色
    color_index: 0,
    color_array: ['白色', '黑色', '深灰色'],

    // 高度
    hight_index: 0,
    hight_array: ['1.0', '1.1', '1.2', '1.3', '1.5'],

    // 规格
    spec_index: 0,
    spec_array: ['05', '06', '07'],

    // 数量
    num: null,

    // 时间
    date_now: util.formatTime(new Date),

    // 调试信息
    debug_info: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // 首先连接服务器
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  },

  /**
   * 输入材质
   */
  picker_material_change: function(e) {
    this.setData({
      material_index: e.detail.value
    }
    )
  },

  /**
   * 输入颜色
   */
  picker_color_change: function (e) {
    this.setData({
      color_index: e.detail.value
    }
    )
  },

  /**
   * 输入高度
   */
  picker_hight_change: function (e) {
    this.setData({
      hight_index: e.detail.value
    }
    )
  },

  /**
   * 输入数量
   */
  bindinput_number: function(e) {
    this.setData({
      num: parseInt(e.detail.value)
    })
  },
  
  /**
   * 输入时间
   */
  picker_date_change: function (e) {
    this.setData({
      date_now: e.detail.value
    }
    )
  },

  /**
   * 入库
   */
  bindtap_button_in_storage: function(e){
    if (this.data.num == null) {
      // 弹窗显示数量不能为空
      wx.showModal({
        title: '错误',
        content: '数量为空！'
      })
    } else {
      wx.request({
        url: 'http://192.168.1.100:8888/in',
        method: 'POST',
        data: {
          record_user: app.globalData.userInfo.nickName,
          material: this.data.material_array[this.data.material_index],
          spec: this.data.spec_array[this.data.spec_index],
          color: this.data.color_array[this.data.color_index],
          hight: this.data.hight_array[this.data.hight_index],
          operation_date: this.data.date_now,
          operation_num: this.data.num
        },
        header: {
          'content-type': 'application/json' // 默认值
        },
        success: function (res) {
          if (res.data.status == true) {
            wx.showToast({
              title: '入库成功！',
              icon: 'success',
              duration: 2000
            })
          }else {
            wx.showModal({
              title: '入库失败！',
              content: '数据库连接错误'
            })
          }
        },
        fail: function (res) {
          wx.showModal({
            title: '入库失败！',
            content: '服务器连接错误'
          })
        }
      })
    }
  },

  /**
   * 出库
   */
  bindtap_button_out_storage: function () {
    if (this.data.num == null) {
      // 弹窗显示数量不能为空
      wx.showModal({
        title: '错误',
        content: '数量为空！'
      })
    } else {
      wx.request({
        url: 'http://192.168.1.100:8888/out',
        method: 'POST',
        data: {
          record_user: app.globalData.userInfo.nickName,
          material: this.data.material_array[this.data.material_index],
          spec: this.data.spec_array[this.data.spec_index],
          color: this.data.color_array[this.data.color_index],
          hight: this.data.hight_array[this.data.hight_index],
          operation_date: this.data.date_now,
          operation_num: this.data.num
        },
        header: {
          'content-type': 'application/json' // 默认值
        },
        success: function (res) {
          if (res.data.status == true) {
            wx.showToast({
              title: '出库成功！',
              icon: 'success',
              duration: 2000
            })
          } else {
            wx.showModal({
              title: '出库失败！',
              content: res.data.msg
            })
          }
        },
        fail: function (res) {
          wx.showModal({
            title: '出库失败！',
            content: '服务器连接错误'
          })
        }
      })
    }
  },

  onClick: function(){
    wx.request({
      url: 'http://192.168.1.100:8888/showstorageall',
      method: 'GET',
      data: {
        record_user: "wxyindaqing",
        material: "301",
        spec: "23",
        color: "黑色",
        hight: "1.3",
        operation_date: "2016-10-2 09:20:32",
        operation_num: 10,
        begin_date: "2016-10-2 09:20:32",
        end_date: "2019-10-2 09:20:32",
        is_in: "1"
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success: function (res) {
        console.log(res.data)
      }
    })
  }
})
