# -*- coding: utf-8 -*-
# Copyright 2014 Bernard Yue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from hanziconv import HanziConv
print(HanziConv.toSimplified('繁簡轉換器'))
# 繁简转换器
print(HanziConv.toTraditional('繁简转换器'))
# 繁簡轉換器
print(HanziConv.same('繁簡轉換器', '繁简转换器'))
# True
print(HanziConv.toSimplified("把中檀元帅固定在神轿"))
print(HanziConv.toSimplified("把中壇元帥固定在神轎"))
# 把中坛元帅固定在神轿
print(HanziConv.toSimplified("洩"))
# 泄
print(HanziConv.toSimplified("湿"))
# 溼
print(HanziConv.toSimplified("淫慾"))
# 淫欲
print(HanziConv.toSimplified("呼吸"))
# 唿吸
print(HanziConv.toSimplified("猛烈"))
# 勐烈
print(HanziConv.toSimplified("四週"))
# 四週
print(HanziConv.toSimplified("猛男该听的歌"))
# 猛男该听的歌
print(HanziConv.toSimplified("呼叫"))
# 呼叫
print(HanziConv.toSimplified("呼"))
# 呼
print(HanziConv.toSimplified("溜"))
# 熘

# test traditional to traditional
print(HanziConv.toTraditional("親愛的牽起你的手 並將他們放在我手中"))
# 親愛的牽起你的手 並將他們放在我手中

# test simplified to simplified
print(HanziConv.toSimplified("把中坛元帅固定在神轿"))
# 把中坛元帅固定在神轿