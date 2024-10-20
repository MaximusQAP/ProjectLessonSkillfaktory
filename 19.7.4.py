def sort_users_by_activity(user_activity):
   sorted_users = sorted(user_activity.items(), key=lambda x: x[1], reverse=True)
   return [user[0] for user in sorted_users]