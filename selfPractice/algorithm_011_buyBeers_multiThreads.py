import threading
import time

class Store:
	def __init__(self, num_beerInStock:int, num_beerSold:int, price_beer:float, ratio_bot_beer:int, ratio_cap_beer:int, money_in:float, num_bot_in:int, num_cap_in:int):
		self.num_beerInStock = num_beerInStock
		self.num_beerSold = num_beerSold
		self.price_beer = price_beer
		self.ratio_bot_beer = ratio_bot_beer
		self.ratio_cap_beer = ratio_cap_beer
		self.money_in = money_in
		self.num_bot_in = num_bot_in
		self.num_cap_in = num_cap_in
	
	def showInfo(self):
		info = (self.num_beerInStock, self.num_beerSold, self.price_beer, self.ratio_bot_beer, self.ratio_bot_beer, self.money_in, self.num_bot_in, self.num_cap_in)
		return("余货:%d \t 已售:%d \t 售价:%d \t 瓶换酒:%d \t 盖换酒:%d \t 入账合计：%d \t 已收酒瓶:%d \t 已收瓶盖:%d" % info)
		
		
class Customer:
	def __init__(self,money_inpocket:float,num_bot:int,num_cap:int,num_dri:int):
		self.money_inpocket = money_inpocket
		self.num_bot = num_bot
		self.num_cap = num_cap
		self.num_dri = num_dri
		
	def showInfo(self):
		info = (self.money_inpocket, self.num_bot, self.num_cap, self.num_dri)
		return("余款:%d \t 有酒瓶:%d \t 有瓶盖:%d \t 已经喝了:%d" % info)
	
	def buy(self,store,num_beer):
		if num_beer > 0:
			if store.num_beerInStock >= num_beer:
				if self.money_inpocket >= num_beer*store.price_beer:
					# 商店操作
					store.num_beerInStock -= num_beer
					store.money_in += num_beer*store.price_beer
					# 消费者操作
					self.money_inpocket -= num_beer*store.price_beer
					self.num_bot += num_beer
					self.num_cap += num_beer
					self.num_dri += num_beer
					# 输出
					return(1,("购买成功！ 买了 %d 瓶" % num_beer))
				else:
					info = (num_beer*store.price_beer, self.money_inpocket, num_beer*store.price_beer-self.money_inpocket)
					return(-1,("购买失败: 钱不够，需要 %d ，但目前只有 %d ，还差 %d ." % info))
			else:
				return(-2,("购买失败: 店里不够了，该店目前只有 %d 瓶了。" % store.num_beerInStock))
		else:
			return(-3,("购买失败: 购买数量应大于0"))
			
	def exchange(self,store,obj,num):
		if obj == 'bot':  # 瓶子换酒
			if store.num_beerInStock >= num/store.ratio_bot_beer:
				if self.num_bot >= num and num >= store.ratio_bot_beer:
					# 计算
					num_beer_exchange = num//store.ratio_bot_beer
					num_obj_exchange = num_beer_exchange*store.ratio_bot_beer
					# 商店操作
					store.num_beerInStock -= num_beer_exchange
					store.num_bot_in += num_obj_exchange
					# 消费者操作
					self.num_bot = self.num_bot - num_obj_exchange + num_beer_exchange
					self.num_cap += num_beer_exchange
					self.num_dri += num_beer_exchange
					# 输出
					return(1,("置换成功！ 换了 %d 个瓶子" % num_obj_exchange))
				else:
					return(0,("置换失败: 你并没有这么多瓶子！"))
			else:
				return(0,("置换失败: 店里不够了，该店目前只有 %d 瓶了。" % store.num_beerInStock))
				
		elif obj == 'cap': # 瓶盖换酒
			if store.num_beerInStock >= num/store.ratio_cap_beer:
				if self.num_cap >= num and num >= store.ratio_cap_beer:
					# 计算
					num_beer_exchange = num//store.ratio_cap_beer
					num_obj_exchange = num_beer_exchange*store.ratio_cap_beer
					# 商店操作
					store.num_beerInStock -= num_beer_exchange
					store.num_cap_in += num_obj_exchange
					# 消费者操作
					self.num_bot += num_beer_exchange
					self.num_cap = self.num_cap - num_obj_exchange + num_beer_exchange
					self.num_dri += num_beer_exchange
					# 输出
					return(1,("置换成功！ 换了 %d 个瓶盖" % num_obj_exchange))
				else:
					return(0,("置换失败: 你并没有这么多瓶盖！"))
			else:
				return(0,("置换失败: 店里不够了，该店目前只有 %d 瓶了。" % store.num_beerInStock))
		else:
			return(0,("只能用瓶子(bot)或者盖子(cap)换！"))


class ArtificialIdiot:
	def __init__(self,store,customer):
		self.store = store
		self.customer = customer
		self.num_steps = 0
	
	def go(self):
		# 购买状态
		flag_managedTo_buy = 1	# 成功购买
		flag_managedTo_bot = 1	# 成功置换-用瓶子
		flag_managedTo_cap = 1	# 成功置换-用瓶盖
		
		while (flag_managedTo_buy + flag_managedTo_bot + flag_managedTo_cap) > 0:
			flag_managedTo_buy = self.customer.buy(self.store,self.customer.money_inpocket//self.store.price_beer)
			if flag_managedTo_buy == 1:
				self.showAllInfo()
			flag_managedTo_bot = self.customer.exchange(self.store,'bot',self.customer.num_bot)
			if flag_managedTo_bot == 1:
				self.showAllInfo()
			flag_managedTo_cap = self.customer.exchange(self.store,'cap',self.customer.num_cap)
			if flag_managedTo_cap == 1:
				self.showAllInfo()
		
		info = (self.customer.num_dri, self.store.num_bot_in, self.store.num_cap_in)
		result1 = ("完事了。。。 一共喝掉了 %d 瓶啤酒，换过 %d 个瓶盖、 %d 个酒瓶子。" % info)
		result2 = ("还剩下 %d 个瓶子， %d 个瓶盖。" % (self.customer.num_bot, self.customer.num_cap))
		return(result1 + "\n" + result2)
	
	def showAllInfo(self):
		print(self.store.showInfo())
		print(self.customer.showInfo())


def thread_job_1(store,customer):	
	# 新建一个文档存储输出结果
	# 初始化一个商店：店内有100瓶酒，已售0瓶，单价2元，2瓶子换一瓶酒，4瓶盖换一瓶酒，已入账0元，已收酒瓶0个，已收瓶盖0个
	store = Store(100,0,2,2,3,0,0,0)
	store.showInfo()

	# 初始化一个买家：有100块钱，有0个瓶子，0个瓶盖，喝了0瓶酒
	customer = Customer(10,0,0,0)
	customer.showInfo()

	AI = ArtificialIdiot(store,customer)
	AI.go()

def thread_job_2():

def thread_job_3():

if __name__ == "__main__":
	added_thread_1 = threading.Thread(target = thread_job_1, name = "job_1")
	added_thread_2 = threading.Thread(target = thread_job_2, name = "job_2")
	added_thread_3 = threading.Thread(target = thread_job_3, name = "job_3")


	