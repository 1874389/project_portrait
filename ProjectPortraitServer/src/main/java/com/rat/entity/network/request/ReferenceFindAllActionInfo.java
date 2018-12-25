package com.rat.entity.network.request;


import com.rat.entity.network.request.base.ActionInfo;

/**
 * author : L.jinzhu
 * date : 2015/8/12
 * introduce : 请求实体
 */
public class ReferenceFindAllActionInfo extends ActionInfo {
    private int pageNumber;
    private int dataGetType;

    public ReferenceFindAllActionInfo(int actionId, int pageNumber, int dataGetType) {
        super(actionId);
        this.pageNumber = pageNumber;
        this.dataGetType = dataGetType;
    }

    public int getPageNumber() {
        return pageNumber;
    }

    public void setPageNumber(int pageNumber) {
        this.pageNumber = pageNumber;
    }

    public int getDataGetType() {
        return dataGetType;
    }

    public void setDataGetType(int dataGetType) {
        this.dataGetType = dataGetType;
    }
}