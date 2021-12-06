/**
 * Author: Isamu Isozaki
 */
import api from './index';

/**
 * 
 * @param {object} param0
 * Get current user 
 */
export function getToken(email, password) {
  return api.get('/user/get_token', {params: {email, password}});
}

export function postUser(email, first_name, last_name, password) {
  return api.post('/user/create', { email, first_name, last_name, password });
}