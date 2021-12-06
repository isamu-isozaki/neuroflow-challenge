/*
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-05T20:25:21.219Z
Modified: !date!
Modified By: modifier
*/
import api from './index';

export function postMood(mood, token) {
    return api.post('/mood',{mood}, {headers: {Authorization: token}});
}

export function getMoods(token) {
    return api.post('/mood',{headers: {Authorization: token}});
}